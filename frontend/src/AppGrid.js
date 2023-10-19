import React, { useState, useEffect } from 'react';

function AppGrid() {
    const [apps, setApps] = useState([]);

    useEffect(() => {
        // Fetch data from the API when the component mounts
        fetch('http://localhost:8000/api/apps')
            .then(response => response.json())
            .then(data => setApps(data.new_ios)); // Assuming new_ios is the only array you want
    }, []);

    return (
        <div>
            <h2>New iOS Apps</h2>
            <div className="app-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                {apps.map(app => (
                    <div className="app-item p-4 border rounded" key={app.id}>
                        <a href={app.store_link} className="block text-center text-black no-underline hover:text-blue-600">
                            <img src={app.icon_url_512} alt={app.name} className="app-icon" />
                            <div>{app.name}</div>
                            {/* You can add a component for the app rating here */}
                        </a>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default AppGrid;