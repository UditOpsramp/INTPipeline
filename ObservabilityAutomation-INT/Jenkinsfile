pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('ObservabilityAutomation') {
      steps {
        sh 'python3 ObservabilityAutomation-INT/LogsAutomation/LogsValidation.py'
      }
    }
  }
} 
