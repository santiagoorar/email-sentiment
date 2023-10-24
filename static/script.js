async function getPrediction() {
    const textInput = document.getElementById("textInput").value;
    const resultDiv = document.getElementById("result");

    try {
        let response = await fetch('/predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "text": textInput
            })
        });

        if (!response.ok) {
            throw new Error("Failed to fetch prediction");
        }

        let data = await response.json();

        if (data.sentiment && data.confidence) {
            resultDiv.innerHTML = `<strong>Sentiment:</strong> ${data.sentiment} <br> <strong>Confidence:</strong> ${data.confidence.toFixed(2)}`;
        } else {
            resultDiv.innerHTML = `<strong>Error:</strong> Unexpected response format`;
        }
    } catch (error) {
        resultDiv.innerHTML = `<strong>Error:</strong> ${error.message}`;
    }
}

