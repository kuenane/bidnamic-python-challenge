
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.orm import relationship
import enum

db = SQLAlchemy()


class selectStatus(enum.Enum):
    ENABLED = "ENABLED"
    REMOVED = "REMOVED"


class Campaign(db.Model):
    """
    A model of the campaign entries
    """

    campaign_id = db.Column(db.BigInteger, primary_key=True)
    structure_value = db.Column(db.String(256), nullable=False)
    status = db.Column(db.String(7), nullable=False)

class SearchTerm(db.Model):
    """
    A representation of a search_term in Flask

    On class
    initilization roas is calculated and a primary key
    is assigned
    """

    # id field will be the hash of foreign keys & date
    search_term_id = db.Column(db.BigInteger,primary_key=True)
    date = db.Column(db.Date,nullable=False)
    children = relationship("ADGROUP", cascade="all,delete", backref="parent")
   
    clicks = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    conversion_value = db.Column(db.BigInteger, nullable=False)
    conversions = db.Column(db.Integer,nullable=False)
    search_term = db.Column(db.String(256), nullable=False)
    roas = db.Column(db.Float, nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Wrapper to set the PK to a hash value & roas on initilization
        """
        super(SearchTerm, self).__init__(*args, **kwargs)
        self.search_term_id = abs(
            hash(
                (
                    self.date,
                    self.ad_group.ad_group_id, # pylint: disable=no-member
                    self.campaign.campaign_id, # pylint: disable=no-member
                    self.search_term,
                )
            )
        )
        if self.cost <= 0:
            self.roas = 0
        else:
            self.roas = self.conversion_value / self.cost

    @staticmethod
    def get_fields() -> set:
        """
        returns all fields field names
        """
        fields = SearchTerm._meta._get_fields( # pylint: disable=no-member,protected-access
            forward=True,
            reverse=False,
            include_parents=False,
            include_hidden=False,
            seen_models=None,
        )
        parsed_fields = set()
        for field in fields:
            parsed_fields.add(str(field).rsplit(".", maxsplit=1))
            #parsed_fields.add(str(field).split(".")[-1])
        return parsed_fields

    @staticmethod
    def query(filters: list[dict()], order_by: str, limit: int) -> dict():
        """
    
        """
        res = {}
        for _filter in filters:
            res[list(_filter.values())[0]] = SearchTerm.objects.filter( # pylint: disable=no-member
                **_filter
            ).order_by(order_by)[:limit]
        return res

class AdGroup(db.Model):
    """
    adgroup type
    Contains additional function 'find_by_alias'
    Which accepts a string and searched for a known
    adgroup alias
    """

    ad_group_id = db.Column(db.BigInteger, primary_key=True)
    # campaign = db.ForeignKey(
    #     "campaigns.Campaign",
    #     on_delete=db.CASCADE,
    # )
    campaigns = relationship("Campaign", cascade="all, delete")
    alias = db.Column(db.String,nullable=False)
    status = db.Column(db.String(7),  nullable=False)

    @staticmethod
    def find_by_alias(alias):
        """
        Find all adgroups that match a given alias
        The alias can either be provided as a string or dictionary with fields:
        alias_fields=['unknown_field','category','region','structure_value',
        'purchase_intent','search_term','uuid_hex']
        """

        try:
            alias_dict = json.loads(alias)
            assert set(alias_dict.keys()).issubset(set(['search_term','uuid_hex']))
            assert len(alias_dict.keys()) == 1
            adgroups = AdGroup.objects.filter(  # pylint: disable=no-member
                **{f"alias__{list(alias_dict.keys())[0]}": list(alias_dict.values())[0]}
            )
        except (ValueError,AssertionError,json.JSONDecodeError,AttributeError):
            parsed_alias = AdGroup.parse_alias(alias)
            adgroups = AdGroup.objects.filter(  # pylint: disable=no-member
                **{"alias__contains": parsed_alias}
            )

        return adgroups

    @staticmethod
    def parse_alias(
        alias: str,
        alias_fields=[
            "unknown_field",
            "category",
            "region",
            "structure_value",
            "purchase_intent",
            "search_term",
            "uuid_hex",
        ],
    ) -> dict:
        """
        Given the alias as a string, parse it into a dictionay
        assuming that each field is obtained by splitting on ' - '
        Input:
            alias: a string, which we expect to have ' - ' delimiters
            alias_fields: a list of field names to be assigned
                        (index of the list maps to the split of ' - ')
        Ouput:
            a dictionary
        Example:
            Input: Shift- Shopping - GB - venum - LOW - monkey-ack-robert-comet - 817ce4
            Output:
            {
                'unknown_field': 'Shift',
                'category': 'Shopping'
                'region': 'GB',
                'structure_value: 'venum',
                'purchase_intent': 'LOW',
                'search_term': 'monkey-ack-robert-comet',
                'uuid_hex':  '817ce4882dfc499886ca8670ccd5cbf9'
            }
        """
        values = alias.split(" - ")
        assert len(alias_fields) == len(
            values
        ), f"alias_fields: {alias_fields}, values: {values}"
        alias_dict = dict()
        for i in range(len(values)): # pylint: disable=consider-using-enumerate
            alias_dict[alias_fields[i]] = values[i]
        return alias_dict