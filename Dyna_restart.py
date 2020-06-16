import json
import requests, csv, os, ssl, time

ENV = ''
TOKEN = ''
ARGS = {'Api-Token':TOKEN} 
PATH = os.getcwd()
current_file_path = os.path.dirname(os.path.realpath(__file__))


def hosts_cnd(list_type, hostid, ENV, ARGS):
    try:
        r = requests.get(ENV + list_type + '/' + hostid + '?', params=ARGS)
        res = r.json()
        print('Entidad {} nombre {}'.format(res['entityId'], res['displayName']))
        return res['displayName']
    except ssl.SSLError:
        print("SSL Error")

def process_restart(list_type, ENV, ARGS):
    try:
        r = requests.get(ENV + list_type + '?', params=ARGS)
        res = r.json()
        for key, value in enumerate(res):
                estado = res[key]['monitoringState']['restartRequired']
                if estado == True:
                    time.sleep(0.6)
                    if 'listenPorts' in value:
                        listenPorts = res[key]['listenPorts']
                    else:
                        listenPorts = 'NO APLICA'
                    if 'softwareTechnologies' in value:
                        softwareTechnologies = res[key]['softwareTechnologies']
                    else:
                        softwareTechnologies = 'NO APLICA'
                    if 'agentVersions' in value:
                        oneAgentVersion = res[key]['agentVersions'][0]['minor']
                    else:
                        oneAgentVersion = 'NO APLICA'
                    with open ( time.strftime("%y_%m_%d_") + "process_bchile_restart.csv", "a", newline="") as f2:
                        writer = csv.writer(f2)
                        idHost = res[key]['fromRelationships']['isProcessOf']
                        servidor = hosts_cnd('hosts', idHost[0], ENV, ARGS)
                        print (oneAgentVersion)
                        writer.writerow([key, servidor, res[key]['entityId'], res[key]['displayName'], res[key]['monitoringState']['restartRequired'], oneAgentVersion, softwareTechnologies, listenPorts])

        f2.close
    except ssl.SSLError:
        print("SSL Error")



if __name__ == "__main__":
    with open(f"{current_file_path}/config.json", "r") as f: 
        config = json.load(f)
        ENV = config["dynatrace_base_url"]
        TOKEN = config["dynatrace_token"]
        ARGS = {'Api-Token':TOKEN} 
    process_restart('processes', ENV, ARGS)
