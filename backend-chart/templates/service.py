apiVersion: v1
kind: Service
metadata:
  name: backend
spec:
  type: NodePort
  selector:
    type: backend
  ports:
    - port: 4000
      targetPort: 4000
