// This file contains the JavaScript code for the frontend, handling user interactions and making API calls to the backend.

document.addEventListener('DOMContentLoaded', function() {
    const queryForm = document.getElementById('query-form');
    const resultsContainer = document.getElementById('results');

    queryForm.addEventListener('submit', async function(event) {
        event.preventDefault();
        const queryInput = document.getElementById('query-input').value;

        if (queryInput) {
            const response = await fetch('/api/desk-query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query: queryInput }),
            });

            if (response.ok) {
                const data = await response.json();
                displayResults(data.recommendations);
            } else {
                resultsContainer.innerHTML = '<p>Error fetching recommendations. Please try again.</p>';
            }
        }
    });

    function displayResults(recommendations) {
        resultsContainer.innerHTML = '';
        if (recommendations.length > 0) {
            recommendations.forEach(rec => {
                const recElement = document.createElement('div');
                recElement.classList.add('recommendation');
                recElement.innerText = `Desk: ${rec.desk}, Location: ${rec.location}, Features: ${rec.features}`;
                resultsContainer.appendChild(recElement);
            });
        } else {
            resultsContainer.innerHTML = '<p>No suitable desks found.</p>';
        }
    }
});