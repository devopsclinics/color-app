// pipeline {
//     agent any

//     options {
//         buildDiscarder(logRotator(numToKeepStr: '5'))
//     }

//     stages {
//         stage('Scan') {
//             steps {
//                 withSonarQubeEnv('sq1') {
//                     sh './mvnw clean org.sonarsource.scanner.maven:sonar-maven-plugin:3.9.0.2155:sonar'
//                 }
//             }
//         }
//     }
// }
pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from the version control system
                checkout scm
            }
        }

        stage('Install SonarQube Scanner') {
            steps {
                // Install the SonarQube Scanner for Python
                sh 'pip install sonar-scanner'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sq1') {
                    sh '''
                        sonar-scanner \
                        -Dsonar.projectVersion=1.0 \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=$SONAR_HOST_URL \
                        -Dsonar.login=$SONAR_TOKEN
                    '''
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace after build
            cleanWs()
        }
    }
}
