pipeline {
  agent any
  
  parameters {
    string(name: 'operatingSystem', description: 'Operating System')
    string(name: 'architecture', description: 'Architecture')
    // Добавьте другие параметры заявки
  }
  
  stages {
    stage('Process Request') {
      steps {
        script {
          sh "python process_request.py ${params.operatingSystem} ${params.architecture}"
        }
      }
    }
    
    // Другие стадии пайплайна
  }
}
