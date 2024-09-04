document.getElementById('uploadForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = new FormData();
    const fileInput = document.querySelector('input[name="file"]');
    
    formData.append("file", fileInput.files[0]);

    const response = await fetch('/uploadfile/', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();

    const resultDiv = document.getElementById('result');
    if (response.ok) {
        resultDiv.innerHTML = `<h3>Uploaded File: ${result.filename}</h3>${result.html_table}`;
    } else {
        resultDiv.innerHTML = `<h3 style="color:red;">Error: ${result.detail}</h3>`;
    }
});
