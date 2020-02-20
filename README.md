# cicdTest


## teamcity

installatie teamcity via docker containers

server:

docker run -it --name teamcity-server-instance \
-v /Users/beppe/teamcity/data:/data/teamcity_server/datadir \
-v /Users/beppe/teamcity/logs:/opt/teamcity/logs \
-p 8080:8111 \
jetbrains/teamcity-server

agent:

docker run -it -e SERVER_URL="localhost:8080" -v /Users/beppe/teamcity/agent/:/data/teamcity_agent/conf jetbrains/teamcity-agent

gewone installatie:

-zorg dat de gewenste tools aanwezig/geconfigureerd zijn (in ons geval docker en helm) op de agent (in ons geval gebruiken we de main server ook als agent)
(copy kubeconfig naar agent voor helm)

-in project settings. voeg docker stappen toe om container images te builden en pushen. voeg stap toe voor helm remove (verwijdert huidig runnende container) en voeg laatste stap toe helm install (specifieer altijd helm config locatie)

voordeel is dat deze kunnen geconfigureerd worden in ide (dus local build settings kunnen geexport worden naar build server als men een intellij ide gebruikt)


## tekton

https://developer.ibm.com/tutorials/deploy-a-hello-world-application-on-kubernetes-using-tekton-pipelines/

https://github.com/tektoncd/pipeline/blob/master/docs/tutorial.md

https://github.com/tektoncd/pipeline/blob/master/docs/install.md

install tekton

kubectl apply --filename https://storage.googleapis.com/tekton-releases/latest/release.yaml

docker config is een configmap gemaakt van config.json wa base64 username:pass inhoud heeft erges


kubectl create clusterrole tutorial-role \
               --verb=get,list,watch,create,update,patch,delete \
               --resource=deployments,deployments.apps,services,pods
               
https://github.com/tektoncd/triggers/blob/master/docs/getting-started/README.md