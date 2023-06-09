pipeline {
  agent any
  
  triggers {
    GenericTrigger(
      genericVariables: [
        [key: 'operatingSystem', value: '$.operating_system'],
        [key: 'architecture', value: '$.architecture']
      ],
      token: 'stig',
      printContributedVariables: true
    )
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
