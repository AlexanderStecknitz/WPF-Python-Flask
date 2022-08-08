from dependency_injector import containers, providers
from services.kunde_read_service import KundeReadService
from services.kunde_write_service import KundeWriteService


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(packages=["rest"])

    config = providers.Configuration()

    kunde_read_service = providers.Factory(
        KundeReadService,
    )

    kunde_write_service = providers.Factory(
        KundeWriteService
    )
