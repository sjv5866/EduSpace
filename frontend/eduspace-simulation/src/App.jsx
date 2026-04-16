import React, { useRef } from "react";
import { Canvas } from "@react-three/fiber";
import Earth from './Earth';
import { Stats, OrbitControls } from '@react-three/drei';

const App = () => {
  return (
    <Canvas camera={{ position: [0, 0, 8.5], fov: 40 }} style={{
      width: "100%",
      height: "100vh",
      objectFit: "cover",
      backgroundImage: "url('./2k_stars.webp')",
      backgroundSize: "cover",
    }}>
      <ambientLight intensity={0.4} color="#fceaff" />
      <Earth position={[0, -0.1, 0]} />
      <OrbitControls enablePan={false} enableDamping={false}/>
      <Stats />
    </Canvas>
  );
};

export default App;
