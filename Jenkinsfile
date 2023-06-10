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
          sh "python -m pip install zipfile argparse"
          def answer = sh"python process_request.py ${genericVariables.operatingSystem} ${genericVariables.architecture}"
          return answer
        }
      }
    }
    
    // Другие стадии пайплайна
  }
}
