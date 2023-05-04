// Add custom JavaScript here

// Get the search form and add event listener for submission
const searchForm = document.querySelector('form');
searchForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent form from submitting normally

  // Get the query input value
  const queryInput = document.querySelector('#query');
  const query = queryInput.value;

  // Send a POST request to the server with the query
  fetch('/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({query: query})
  })
  .then(response => response.json())
  .then(data => {
    // Update the results table with the new data
    const resultsTable = document.querySelector('table tbody');
    resultsTable.innerHTML = '';
    data.results.forEach(result => {
      const row = document.createElement('tr');
      const ipAddress = document.createElement('td');
      ipAddress.textContent = result.ip_str;
      const port = document.createElement('td');
      port.textContent = result.port;
      const data = document.createElement('td');
      data.textContent = result.data;
      row.appendChild(ipAddress);
      row.appendChild(port);
      row.appendChild(data);
      resultsTable.appendChild(row);
    });

    // Update the count of results
    const count = document.querySelector('#count');
    count.textContent = data.count;
  })
  .catch(error => console.error(error));
});
