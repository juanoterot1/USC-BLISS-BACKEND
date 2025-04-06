class UsageLogService:
    def create_usage_log(self, action, performed_by=None):
        # Implementación de la lógica para registrar logs de uso
        print(f"Log: {action} by {performed_by}")
