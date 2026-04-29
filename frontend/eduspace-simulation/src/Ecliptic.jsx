import { useEffect, useLayoutEffect, useMemo, useRef, useState } from 'react';
import { useFrame } from '@react-three/fiber';
import * as THREE from 'three';

export default function Ecliptic({ radius = 2, speed = 1 }) {
  const pointRef = useRef();
  const lastCall = useRef(0);

  useFrame((state, delta) => {
    if (pointRef.current) {
        const now = Date.now();
        if (now - lastCall.current > 1000) {
          lastCall.current = now;
          fetch('http://localhost:5000/tles/pos/POISK')
            .then(res => res.json())
            .then(data => {
              console.log(data);
              pointRef.current.position.x = data.x;
              pointRef.current.position.y = data.y;
              pointRef.current.position.z = data.z;
            });
        }
        
    }
  });

  return (
    <mesh ref={pointRef}>
      <sphereGeometry args={[0.2, 16, 16]} />
      <meshStandardMaterial color="yellow" />
    </mesh>
  );
}