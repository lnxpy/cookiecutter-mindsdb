from typing import List

import pandas as pd
from mindsdb.integrations.libs.api_handler import APIHandler, APITable
from mindsdb_sql.parser import ast


class SampleTable(APITable):
    name: str = "sample"
    columns: List[str] = ...

    def __init__(self, handler: APIHandler):
        super().__init__(handler)
        self.handler.connect()

    def select(self, query: ast.Select) -> pd.DataFrame:
        """triggered at the SELECT query

        Args:
            query (ast.Select): user's entered query

        Returns:
            pd.DataFrame: the queried information
        """
        ...

    def get_columns(self, ignore: List[str] = []) -> List[str]:
        """columns

        Args:
            ignore (List[str], optional): exclusion items. Defaults to [].

        Returns:
            List[str]: available columns with `ignore` items removed from the list.
        """

        return [item for item in self.columns if item not in ignore]
