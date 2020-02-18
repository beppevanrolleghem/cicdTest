# cicdTest


## teamcity

voor teamcity was het opstellen van de server heel simpel aangezien dit via een docker container kan.
Er moet wel een aparte agent opgesteld worden, maar dit kan ook via een docker container.

server:

docker run -it --name teamcity-server-instance \
-v /Users/beppe/teamcity/data:/data/teamcity_server/datadir \
-v /Users/beppe/teamcity/logs:/opt/teamcity/logs \
-p 8080:8111 \
jetbrains/teamcity-server

agent:

docker run -it -e SERVER_URL="localhost:8080" -v /Users/beppe/teamcity/agent/:/data/teamcity_agent/conf jetbrains/teamcity-agent

de reden dat we een agent nodig hebben is om docker images te builden en pushen. 




## tekton

https://developer.ibm.com/tutorials/deploy-a-hello-world-application-on-kubernetes-using-tekton-pipelines/

https://github.com/tektoncd/pipeline/blob/master/docs/tutorial.md

https://github.com/tektoncd/pipeline/blob/master/docs/install.md

install tekton

kubectl apply --filename https://storage.googleapis.com/tekton-releases/latest/release.yaml

docker config is een configmap gemaakt van config.json wa base64 username:pass inhoud heeft erges
