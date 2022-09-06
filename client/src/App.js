import React, { useState } from "react";
import axios from "axios";
import { Icon } from "leaflet";
import { Alert, Spinner } from "react-bootstrap";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import useSwr from "swr";
import "./App.css";
import useSWR from "swr";

export const icon = new Icon.Default();

const fetcher = (url) => axios.get(url).then((res) => res.data)

const App = () => {
  const [activeHospital, setActiveHospital] = useState(null);
  const { data, error } = useSWR('/api/v1/hospitals', fetcher)
  const hospitals = data && !error ? data : {}
  const position = [-1.94, 29.87]
  const zoom = 9

  if (error) {
    return <Alert variant="danger">YOU are a problem.</Alert>
  }

  if (!data) {
    return (
      <Spinner animation="border" role="status">
        <span className="visually-hidden">Loading...</span>
      </Spinner>
    );
  }

  return (
    <MapContainer center={position} zoom={zoom}>
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {hospitals.features.map((hospital) => (
        <Marker
          key={hospital.properties.name}
          position={[
            hospital.geometry.coordinates[1],
            hospital.geometry.coordinates[0],
          ]}
          onClick={() => {
            setActiveHospital(hospital);
          }}
          icon={icon}
        >
          <Popup
            position={[
              hospital.geometry.coordinates[1],
              hospital.geometry.coordinates[0],
            ]}
            onClose={() => {
              setActiveHospital(null);
            }}
          >
            <div>
              <h6>{hospital.properties.name}</h6>
            </div>
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

export default App