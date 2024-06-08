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

        stage('Verify Java Installation') {
            steps {
                // Print Java version for debugging
                sh '''
                    java -version
                '''
            }
        }

        stage('Verify SonarQube Scanner Installation') {
            steps {
                // Verify SonarQube Scanner installation
                sh '''
                    if [ ! -x /opt/sonar-scanner-5.0.1.3006-linux/bin/sonar-scanner ]; then
                        echo "SonarQube Scanner not found or not executable"
                        exit 1
                    fi
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sq2') {
                    sh '''
                        export SONAR_SCANNER_OPTS="-Djavax.net.ssl.trustStorePassword=changeit"
                        /opt/sonar-scanner-5.0.1.3006-linux/bin/sonar-scanner \
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

