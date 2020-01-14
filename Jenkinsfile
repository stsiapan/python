def remote_user = "vagrant"
def remote_ip = "192.168.143.154"
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checkout..'
                checkout scm
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                withCredentials([sshUserPrivateKey(credentialsId: 'publisher', keyFileVariable: 'identity', passphraseVariable: '', usernameVariable: 'userName')]) {
                    sshagent(['publisher']) {
                         sh "scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ${WORKSPACE}/monitor.py ${remote_user}@${remote_ip}:/tmp"
                         sh "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ${remote_user}@${remote_ip} 'sudo python /tmp/monitor.py'"
                         sh "scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ${remote_user}@${remote_ip}:/tmp/monitor.py ${WORKSPACE}/"
                         
                    }
                }
            }
        }
        stage('Rich text publisher') {
            steps {
              parserName ('HTML')
              stableText ("${FILE:monitor.py"})                
            }
        }        

    }

}
