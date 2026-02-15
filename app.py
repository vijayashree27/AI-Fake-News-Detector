import boto3
import json

# Creating the Bedrock client
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def check_news(text):
    prompt = f"""
    Analyze the following news text and classify it as Real, Fake, or Biased.
    Also give a credibility score from 0 to 100 and short explanation.

    News: {text}
    """

    response = bedrock.invoke_model(
        modelId="amazon.titan-text-lite-v1",
        body=json.dumps({
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 200,
                "temperature": 0.5
            }
        })
    )

    result = json.loads(response['body'].read())
    return result

if __name__ == "__main__":
    text = input("Enter news text: ")
    output = check_news(text)
    print(output)
