"""Tests for Chatbot deployment manifests."""
import base64
import unittest
from pumpwood_deploy.type import (
    PumpwoodDeployDeployment, PumpwoodDeploySecret)
from pumpwood_deploy_chatbot.deploy import PumpWoodChatbotMicroservice


class TestPumpWoodChatbotMicroservice(unittest.TestCase):
    """Validate generated chatbot Kubernetes manifests."""

    def test__create_files(self):
        """Ensure manifests include secrets, app, and one worker."""
        deploy_obj = PumpWoodChatbotMicroservice(
            microservice_password="xxxx",
            agent_microservice_username="restricted-agent",
            agent_microservice_password="agent-password",
            app_version="xxxx",
            worker_version="xxxx",
            api_key="xxxx")
        results = deploy_obj.create_deployment_file()
        self.assertEqual(len(results), 3)
        self.assertIsInstance(results[0], PumpwoodDeploySecret)
        self.assertEqual(results[0].name, 'pumpwood_chatbot__secrets')
        self.assertIn('openai_api_key', results[0].content)
        self.assertIsInstance(results[1], PumpwoodDeployDeployment)
        self.assertEqual(results[1].name, 'pumpwood_chatbot__deploy')
        self.assertIsInstance(results[2], PumpwoodDeployDeployment)
        self.assertEqual(results[2].name, 'pumpwood_chatbot__worker')
        self.assertIn('OPENAI_API_KEY', results[2].content)
        self.assertIn(
            'value: "restricted-agent"', results[2].content)
        encoded_agent_password = base64.b64encode(
            b"agent-password").decode()
        self.assertIn(encoded_agent_password, results[0].content)
        for item in results:
            self.assertTrue(hasattr(item, 'content'))
            self.assertTrue(len(item.content) > 0)
            self.assertIn('apiVersion', item.content)
            self.assertIn('chatbot', item.content)
