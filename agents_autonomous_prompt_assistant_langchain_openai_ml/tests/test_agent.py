"""
Test script for the LangChain agent.
"""

import unittest
from src import agent

class TestAgent(unittest.TestCase):
    def test_qa_chain(self):
        qa = agent.load_qa_chain()
        self.assertIsNotNone(qa)
        response = qa.run("How do I reset my password?")
        self.assertTrue("password" in response.lower())

if __name__ == "__main__":
    unittest.main()
