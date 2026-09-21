"""Kubernetes deployment package for the Pumpwood Chatbot microservice.

Use ``PumpWoodChatbotMicroservice`` with ``DeployPumpWood`` from
``pumpwood-deploy`` to generate and apply chatbot manifests.

Example:
    ```python
    from pumpwood_deploy_chatbot import PumpWoodChatbotMicroservice

    chatbot = PumpWoodChatbotMicroservice(
        app_version="1.0",
        worker_version="1.0",
        api_key="sk-...",
    )
    deploy.add_microservice(chatbot)
    ```

Cluster prerequisites include ``StandardMicroservices`` (storage
ConfigMap, general secrets, RabbitMQ), ``PumpWoodAuthMicroservice`` for
authorization, and Postgres via ``PGBouncerDatabase``.
"""
from .deploy import PumpWoodChatbotMicroservice

__all__ = [
    PumpWoodChatbotMicroservice
]
