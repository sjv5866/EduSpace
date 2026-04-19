import { useEffect, useLayoutEffect, useMemo, useRef, useState } from 'react';
import { useFrame } from '@react-three/fiber';
import * as THREE from 'three';

export default function Ecliptic({ radius = 2, speed = 1 }) {
  const pointRef = useRef();

  useFrame((state, delta) => {
    if (pointRef.current) {
        /** 
         * Next Steps
         * 1. grab x,y,z position from API HERE. Or from a service class
         * 2. change radius of rotation with respect to TLE via skyfield sgp4 feature.
         * 3. keep speed static or toggle with scrollbar in menu
         */

        // simple orbit example wrt time
        const time = state.clock.elapsedTime * speed;
        pointRef.current.position.x = Math.cos(time) * radius;
        pointRef.current.position.z = Math.sin(time) * radius;
        pointRef.current.position.y = 0;
    }
  });

  return (
    <mesh ref={pointRef}>
      <sphereGeometry args={[0.2, 16, 16]} />
      <meshStandardMaterial color="yellow" />
    </mesh>
  );
}