pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[credentialsId: '59415612', url: 'https://github.com/tejasruu/DEVOPSAI.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: '59415612', url: 'https://github.com/tejasruu/DEVOPSAI.git'
                bat 'python sort.py'
                
            }
        }
        stage('Test') {
            steps {
                echo "Testing is done"
            }
        }
    }
}
