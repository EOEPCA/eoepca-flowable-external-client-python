from flowable.external_worker_client.engine_rest_variable import EngineRestVariable
from flowable.external_worker_client.external_worker_job_response import ExternalWorkerJobResponse


class ExternalWorkerAcquireJobResponse(ExternalWorkerJobResponse):

    def __init__(self, variables: list[EngineRestVariable], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variables = variables
        self.job_vars = {}
        for v in self.variables:
            self.job_vars[v.name] = v.value        

    def get_variable(self, name: str) -> str | None:
        if name in self.job_vars:
            return self.job_vars[name]
        else:
            return None        
