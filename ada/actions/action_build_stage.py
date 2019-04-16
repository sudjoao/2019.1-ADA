from rasa_core_sdk import Action
import requests
import os
import random
from rasa_core_sdk.events import SlotSet

GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")


class BuildStage(Action):
    def name(self):
        return "action_build_stage"

    def run(self, dispatcher, tracker, domain):
        is_there_any_build = False
        try:
          dispatcher.utter_message("Certo! Encontrei a seguinte build no seu \
                                    repositório\n\n:")
          headers = {
              'Content-Type': 'application/json',
          }
          project_owner = "adabot"
          project_name = "ada-gitlab"
          response = requests.get(GITLAB_SERVICE_URL + "jobs/{project_owner}/{project_name}".format(
              project_owner=project_owner, project_name=project_name), headers=headers)
          requests_build = response.json()
        #   for i in range(3):
          dispatcher.utter_message(f"A build {requests_build[0]['name']} está no \
                                     estágio {requests_build[0]['stage']}.\n\n\
                                     O status atual dela é {requests_build[0]['status']}.")
          dispatcher.utter_message(f"Você pode encontrar mais informações sobre essa \
                                    build no seguinte endereço:\n\
                                    {requests_build[i]['web_url']}")
          #dispatcher.utter_message(requests_build[0]['name'])
          #dispatcher.utter_message(requests_build[0]['stage'])
          #dispatcher.utter_message(requests_build[0]['status'])
          # dispatcher.utter_message(requests_build[i]['pipeline/ref'])
          # dispatcher.utter_message(requests_build[i]['web_url'])
          is_there_any_build = True
        except ValueError:
            dispatcher.utter_message(ValueError)
            if(not is_there_any_build):
                default = "Não há build's em andamento, \
                mas continuo te informando.\n"
                dispatcher.utter_message(default)
