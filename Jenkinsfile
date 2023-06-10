pipeline {
  agent any
  
  parameters {
        string(name: 'architecture', description: 'Architecture parameter')
        string(name: 'operating_system', description: 'Operating System parameter')
  }
  
  stages {
    stage('Process Request') {
      steps {
        script {
          bat "python -m pip install argparse"
          def answer = bat "python process_request.py ${params.operating_system} ${params.architecture}"
          return answer
        }
      }
    }
    
    // Другие стадии пайплайна
  }
}
