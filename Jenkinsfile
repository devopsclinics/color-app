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
// }pipeline {
pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from your version control system
                checkout scm
            }
        }

        stage('Install SonarQube Scanner') {
            steps {
                // Download and install the SonarQube Scanner CLI
                sh '''
                    if [ ! -d "sonar-scanner-cli" ]; then
                        wget -qO- https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip | busybox unzip -
                        mv sonar-scanner-5.0.1.3006-linux sonar-scanner-cli
                        chmod +x sonar-scanner-cli/bin/sonar-scanner
                    fi
                '''
            }
        }

        stage('Verify Java Installation') {
            steps {
                // Print Java version for debugging
                sh '''
                    java -version
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sq2') {
                    sh '''
                        ./sonar-scanner-cli/bin/sonar-scanner \
                        -Dsonar.projectVersion=1.0 \
                        -Dsonar.sources=.
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
