import React, { useState } from 'react';
import '../css/Menu.module.css';

const Menu = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [console1, setConsole1] = useState('');
  const [console2, setConsole2] = useState('');

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleExecute = () => {
    // Lógica para enviar una solicitud POST a la API con el archivo seleccionado
    // y obtener los resultados línea por línea
    // Actualizar las consolas con los resultados obtenidos
    setConsole1('Resultado de la ejecución línea por línea...');
  };

  const handleReport = () => {
    // Lógica para obtener el reporte
    // Actualizar la consola con el reporte obtenido
    setConsole2('Reporte...');
  };

  const handleLogout = () => {
    window.location.href="./";
  };

  return (
    <div className="menu-container">
    <input type="file" accept=".mia" onChange={handleFileChange} />
    <div className="console-container">
      <div>
        <h2>Consola 1</h2>
        <textarea value={console1} readOnly />
      </div>
      <div>
        <h2>Consola 2</h2>
        <textarea value={console2} readOnly />
      </div>
    </div>
    <div className="button-container">
      <button onClick={handleExecute}>Ejecutar</button>
      <button onClick={handleReport}>Reporte</button>
      <button onClick={handleLogout}>Logout</button>
    </div>
  </div>
  );
};

export default Menu;
