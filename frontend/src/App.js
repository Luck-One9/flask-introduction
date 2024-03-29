import React, { useEffect, useState } from 'react';

function App() {
  const [name, setName] = useState('...');
  var url = (process.env.REACT_APP_BACKEND_URL ?? "http://localhost:5000")+"/api/name";

  useEffect(() => {
    fetch(url)
      .then(resp => {
        if (!resp.ok) {
          throw new Error('Erro ao recuperar os dados.');
        }
        return resp.text();
      })
      .then(data => {
        setName(data+'!')
      })
      .catch(error => {
        console.error('Ocorreu um erro:', error);
      });
  });

  return (
    <>
      <h1>Hello, { name }</h1>
    </>
  );
}

export default App;
