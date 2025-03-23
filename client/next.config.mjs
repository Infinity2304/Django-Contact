/** @type {import('next').NextConfig} */
const nextConfig = {

    async rewrites() {
        return [
          {
            source: '/api/:path*', // Match requests to /api/*
            destination: 'http://localhost:8080/api/:path*', // Forward to your backend
          },
        ];
      },
};

export default nextConfig;
