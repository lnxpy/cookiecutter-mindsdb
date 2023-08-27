from mindsdb.integrations.handlers.{{cookiecutter.handler_slug}}_handler.{{cookiecutter.handler_slug}}_tables import SampleTable
from mindsdb.integrations.libs.api_handler import APIHandler
from mindsdb.integrations.libs.response import HandlerStatusResponse as StatusResponse
from mindsdb_sql import parse_sql


class {{cookiecutter.handler_name.replace(" ", "")}}Handler(APIHandler):
    def __init__(self, name: str, **kwargs) -> None:
        """initializer method

        Args:
            name (str): handler name
        """
        super().__init__(name)

        self.connection = None
        self.is_connected = False

        _tables = [
            SampleTable,
        ]

        for Table in _tables:
            self._register_table(Table.name, Table(self))

    def check_connection(self) -> StatusResponse:
        """checking the connection

        Returns:
            StatusResponse: whether the connection is still up
        """
        ...

    def connect(self):
        """making the connectino object
        """
        ...

    def native_query(self, query: str) -> StatusResponse:
        """Receive and process a raw query.

        Parameters
        ----------
        query : str
            query in a native format

        Returns
        -------
        StatusResponse
            Request status
        """
        ast = parse_sql(query, dialect="mindsdb")
        return self.query(ast)
