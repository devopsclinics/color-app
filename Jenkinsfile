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

    environment {
        JAVA_HOME = '/opt/jdk-13.0.1'
        PATH = "${JAVA_HOME}/bin:${env.PATH}"
    }

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
                // Download and install the SonarQube Scanner CLI
                sh '''
                    if [ ! -d "sonar-scanner-cli" ]; then
                        wget -qO- https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.6.2.2472-linux.zip | busybox unzip -
                        mv sonar-scanner-4.6.2.2472-linux sonar-scanner-cli
                        chmod +x sonar-scanner-cli/bin/sonar-scanner
                    fi
                '''
            }
        }

        stage('Verify Environment Variables') {
            steps {
                // Print JAVA_HOME and PATH for debugging
                sh '''
                    echo "JAVA_HOME: $JAVA_HOME"
                    echo "PATH: $PATH"
                    java -version
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sq1') {
                    sh '''
                        export JAVA_HOME=/opt/jdk-13.0.1
                        export PATH=$JAVA_HOME/bin:$PATH
                        ./sonar-scanner-cli/bin/sonar-scanner \
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
