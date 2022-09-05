import React from "react"
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet"
import "./App.css"

const App = () => {
  return (
    <MapContainer center={[-1.94, 29.87]} zoom={9}>
    <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
    </MapContainer>
  );
};

export default App