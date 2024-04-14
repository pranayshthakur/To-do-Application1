node
{
    
    stage('code checkout')
    {
        git branch: 'main', url: 'https://github.com/rajraviojha/To-Do-Application-Deployment.git' 
    }
    
    stage ('containerize')
    {
        sh 'docker build -t jharajltp'
    }
    
     stage('push to dockerhub')
        {
         
         withCredentials([string(credentialsId: 'dockerPwd', variable: 'dockerHubPwd')])
            {
                sh "docker login -u <username> -p ${dockerHubPwd}"
                sh 'docker push <username/dockerimage name>'
            }
         
        }
     
     stage('Deploy')
    {
         ansiblePlaybook become: true, credentialsId: 'ansible-ssh-jenkins-key', disableHostKeyChecking: true, installation: 'ansible', inventory: '/etc/ansible/hosts', playbook: 'playbook.yml', vaultTmpPath: ''
     }
     
}