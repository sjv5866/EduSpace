import { useEffect, useLayoutEffect, useMemo, useRef, useState } from 'react';
import { useFrame } from '@react-three/fiber';
import * as THREE from 'three';

export default function Ecliptic({ radius = 2, speed = 1 }) {
  const pointRef = useRef();
  const lastCall = useRef(0);

  useFrame((state, delta) => {
    if (pointRef.current) {
        /** 
         * Next Steps
         * 1. grab x,y,z position from API HERE. Or from a service class
         * 2. change radius of rotation with respect to TLE via skyfield sgp4 feature.
         * 3. keep speed static or toggle with scrollbar in menu
         */
        const now = Date.now();
        if (now - lastCall.current > 1000) {
          lastCall.current = now;
          fetch('http:localhost:5000/tles/pos/POISK')
            .then(res => {
              console.log(res);
              return res.json();
            })
            .then(json => {
              console.log(json);
              pointRef.current.position.x = json.x;
              pointRef.current.position.y = json.y;
              pointRef.current.position.z = json.z;
            });
        }

        // simple orbit example wrt time
        // const time = state.clock.elapsedTime * speed;
        
    }
  });

  return (
    <mesh ref={pointRef}>
      <sphereGeometry args={[0.2, 16, 16]} />
      <meshStandardMaterial color="yellow" />
    </mesh>
  );
}