import React from 'react';
import Link from 'next/link';
import { useRouter } from 'next/router';

interface HeaderProps {
  // No specific props needed for this basic header, auth state will come from context
}

const Header: React.FC<HeaderProps> = () => {
  const router = useRouter(); // Initialize router for potential redirects after logout
  
  // Simulate authentication state. In a real app, this would come from a global state/context (e.g., React Context, Zustand, Redux).
  const isAuthenticated: boolean = false; // Currently hardcoded for initial display.
                                         // Will be replaced by actual auth state from backend.

  const handleLogout = () => {
    // In a real application, this would involve:
    // 1. Making an API call to a logout endpoint on the backend.
    // 2. Clearing any local authentication tokens (e.g., from localStorage, cookies).
    // 3. Updating the global authentication state.
    // 4. Redirecting the user to the homepage or login page.
    
    console.log("Attempting to log out...");
    // For now, simulate a redirect to home after a "logout" action
    router.push('/'); 
  };

  return (
    <header className="bg-gradient-to-r from-gray-900 to-slate-800 text-white shadow-lg">
      <nav className="container mx-auto px-4 py-4 flex justify-between items-center">
        {/* Logo / App Name */}
        <div className="flex items-center">
          <Link href="/" className="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600 hover:from-purple-300 hover:to-pink-500 transition-colors duration-200">
            CodeVault
          </Link>
        </div>

        {/* Navigation Links */}
        <div className="flex items-center space-x-6">
          <NavLink href="/">Home</NavLink>
          {isAuthenticated ? (
            <>
              <NavLink href="/dashboard">Dashboard</NavLink>
              <button
                onClick={handleLogout}
                className="py-2 px-4 rounded-md bg-red-600 hover:bg-red-700 text-white font-medium transition-colors duration-200"
              >
                Logout
              </button>
            </>
          ) : (
            <>
              <NavLink href="/login">Login</NavLink>
              <NavLink href="/register" isPrimary>
                Register
              </NavLink>
            </>
          )}
        </div>
      </nav>
    </header>
  );
};

// Helper component for navigation links
interface NavLinkProps {
  href: string;
  children: React.ReactNode;
  isPrimary?: boolean;
}

const NavLink: React.FC<NavLinkProps> = ({ href, children, isPrimary = false }) => (
  <Link href={href} className="flex items-center">
    <span
      className={`
        text-white hover:text-purple-300 transition-colors duration-200
        ${isPrimary ? 'py-2 px-4 rounded-md bg-purple-600 hover:bg-purple-700 font-medium' : ''}
      `}
    >
      {children}
    </span>
  </Link>
);

export default Header;
