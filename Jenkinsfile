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
          bat "python -m pip install zipfile argparse"
          def answer = bat "python process_request.py ${genericVariables.operatingSystem} ${genericVariables.architecture}"
          return answer
        }
      }
    }
    
    // Другие стадии пайплайна
  }
}
