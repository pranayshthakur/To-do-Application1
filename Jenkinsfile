pipeline {
    agent any

    
    stages{
        stage("Code Checkout"){
            steps {
                echo "cloning the code"
                git url:"https://github.com/pranayshthakur/To-do-Application1.git", branch: "main"
            }
            
        }
        
        stage("build docker image"){
            steps {
                echo "Bulding the image"
                sh "docker build -t pythonapp1 ."
            }
            
        }
        
        stage("Push To Docker Hub"){
            steps {
                echo "pushing to docker hub"
                withCredentials([usernamePassword(credentialsId:"dockerid",passwordVariable:"dockeridPass",usernameVariable:"dockeridUser")]){
                sh "docker tag pythonapp1 ${env.dockeridUser}/pythonapp1:1.0"
                sh "docker login -u ${env.dockeridUser} -p ${env.dockeridPass}"
                sh "docker push ${env.dockeridUser}/pythonapp1:1.0"
                }
                
            }
            
        }
        
        stage("Deploy"){
            steps {
                echo "deploy to container"
                sh "docker run -d -p 5000:5000 frupru/pythonapp1:1.0"
                
            }
            
        }

        stage("Selenium Test") {
            steps {
                echo "Running Selenium tests"
                sh "python selenium.py"
            }
        }
        
    }
    
    
}