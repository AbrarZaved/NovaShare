# NovaShare

NovaShare is a **secure file sharing platform** built with **Django**, designed for encrypted file uploads and controlled access. It ensures confidentiality and integrity in file transfers, making it ideal for sensitive data sharing.

## Features

- **Encrypted File Uploads**: Ensures secure storage and transfer of files.
- **Access Control**: Restricts file access based on user permissions.
- **User Authentication**: Secure login system for authorized users.
- **File Expiry & Deletion**: Option to auto-delete files after a set duration.
- **Activity Logs**: Tracks file access and sharing history.
- **REST API Support**: Allows integration with other applications.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL/MySQL (configurable)
- **Frontend**: Django Templates / JavaScript (extendable)
- **Encryption**: AES/RSA for file security

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/NovaShare.git
   cd NovaShare
   ```

2. **Create & Activate a Virtual Environment:**
   ```sh
   python -m venv myenv
   source myenv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:** (Create a `.env` file)
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=your_database_url
   ```

5. **Run Migrations:**
   ```sh
   python manage.py migrate
   ```

6. **Create a Superuser (Optional):**
   ```sh
   python manage.py createsuperuser
   ```

7. **Start the Server:**
   ```sh
   python manage.py runserver
   ```

## Usage

- **Upload & Share Files Securely**: Users can upload files with encryption and set access permissions.
- **Manage Access**: Admins can control file access and set expiration policies.
- **Monitor Activity**: Track file downloads and sharing logs.

## Security Measures

- **End-to-End Encryption** using AES/RSA.
- **User Authentication & Authorization** via Django's built-in system.
- **Secure File Storage** with access controls.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to your branch (`git push origin feature-branch`)
5. Open a pull request

## License

NovaShare is licensed under the **MIT License**.

## Contact

For questions or support, reach out via AbrarZaved[abrarzaved2002@gmail.com].

