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
        sh 'python3 LogsAutomation/LogsValidation.py'
        sh 'python3 TracingAutomation/TracingValidation.py'
      }
    }
  }
} 
