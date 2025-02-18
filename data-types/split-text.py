text = "we are learning Python of Devops"
new_text = text.split()
print("split lines into single words:", new_text)

arn = "partition:service:region:account-id:resource-type/resource-id"
new_arn = arn.split("/")
print("new arn:", new_arn)