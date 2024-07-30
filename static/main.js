// document.addEventListener('DOMContentLoaded', function() {
//     fetch('/api/cloud-count')
//     .then(response => response.json())
//     .then(data => {
//       console.log('Data received:', data); // Debugging line
//       if (data.count !== undefined) {
//         document.getElementById('cloud-count').innerText = 'Clouds: ' + data.count;
//       } else {
//         document.getElementById('cloud-count').innerText = 'Error loading cloud count';
//       }
//     })
//     .catch(error => {
//       console.error('Error fetching cloud count:', error);
//       document.getElementById('cloud-count').innerText = 'Error loading cloud count';
//     });

    // const searchButton = document.getElementById('search-button');
    // const cloudName = document.getElementById('cloud-search');
    // const cloudDetails = document.getElementById('cloud-details');

    // searchButton.addEventListener('click', () => {
    //     const name = cloudName.value.trim();
    //     if (name) {
    //         fetch(`/get-cloud-details?name=${encodeURIComponent(name)}`)
    //             .then(res => res.json())
    //             .then(data => {
    //                 if (data.error) {
    //                     cloudDetails.innerHTML = `<p>Error: ${data.error}</p>`;
    //                 } else {
    //                     cloudDetails.innerHTML = `
    //                         <h3>Cloud Details:</h3>
    //                         <table border="1">
    //                             <tr>
    //                                 <th>Name</th>
    //                                 <td>${data.name}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>Email</th>
    //                                 <td>${data.email}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>CC Mail IDs</th>
    //                                 <td>${data.cc_mail_ids}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>URL</th>
    //                                 <td>${data.url}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>Datacenter Main</th>
    //                                 <td>${data.datacenter_main}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>Datacenters Remote</th>
    //                                 <td>${data.datacenters_remote}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>Role</th>
    //                                 <td>${data.role}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>Status</th>
    //                                 <td>${data.status}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>SFDX Name</th>
    //                                 <td>${data.sfdc_name}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>SFDX ID</th>
    //                                 <td>${data.sfdc_id}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>Private Device Licenses</th>
    //                                 <td>${data.private_device_licenses}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>Shared Devices Licenses</th>
    //                                 <td>${data.shared_devices_licenses}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>Browser Licenses</th>
    //                                 <td>${data.browser_licenses}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>Virtual Device Licenses</th>
    //                                 <td>${data.virtual_device_licenses}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>Cloud Build</th>
    //                                 <td>${data.cloud_build}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>Reporter Build</th>
    //                                 <td>${data.reporter_build}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>NV Build</th>
    //                                 <td>${data.nv_build}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>Selenium Build</th>
    //                                 <td>${data.selenium_build}</td>
    //                             </tr>
    //                             <tr>
    //                                 <th>Phase</th>
    //                                 <td>${data.phase}</td>
    //                             </tr>
    //                         </table>
    //                     `;
    //                 }
    //             })
    //             .catch(err => {
    //                 cloudDetails.innerHTML = `<p>Error fetching cloud details: ${err}</p>`;
    //             });
    //     } else {
    //         cloudDetails.innerHTML = `<p>Please enter a cloud name</p>`;
    //     }
    // });
// });
