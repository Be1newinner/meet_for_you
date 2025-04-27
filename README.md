# Social Media App

## Routes

### **1. Auth Routes**
Handles user authentication and token management.

| Method | Route               | Description                          |
|--------|---------------------|--------------------------------------|
| POST   | `/api/auth/register` | Register a new user                  |
| POST   | `/api/auth/login`    | Login and return access & refresh JWTs |
| POST   | `/api/auth/logout`   | Logout user (invalidate refresh token) |
| POST   | `/api/auth/refresh`  | Get new access token using refresh token |

---

### **2. User Routes**
User profile, settings, and search.

| Method | Route                        | Description                            |
|--------|------------------------------|----------------------------------------|
| GET    | `/api/users/me`              | Get logged-in user profile             |
| PATCH  | `/api/users/me`              | Update own profile                     |
| GET    | `/api/users/:username`       | Get public user profile by username    |
| POST   | `/api/users/avatar`          | Upload/change profile picture          |
| GET    | `/api/users/search?q=`       | Search users by username/full name     |

---

### **3. Post Routes**
Image/video posts like Instagram Feed.

| Method | Route                    | Description                             |
|--------|--------------------------|-----------------------------------------|
| POST   | `/api/posts`             | Create a new post (image/video + caption) |
| GET    | `/api/posts/:id`         | Get a single post                       |
| DELETE | `/api/posts/:id`         | Delete a post                           |
| PATCH  | `/api/posts/:id`         | Edit a post (caption only)              |
| GET    | `/api/posts/user/:username` | Get all posts by a user             |
| GET    | `/api/posts/feed`        | Get feed (from followed users)          |

---

### **4. Like Routes**
Like/unlike system for posts.

| Method | Route                   | Description                        |
|--------|-------------------------|------------------------------------|
| POST   | `/api/likes/:postId`    | Like a post                        |
| DELETE | `/api/likes/:postId`    | Unlike a post                      |
| GET    | `/api/likes/:postId`    | Get all likes for a post           |

---

### **5. Comment Routes**
Commenting system for posts.

| Method | Route                        | Description                        |
|--------|------------------------------|------------------------------------|
| POST   | `/api/comments/:postId`      | Add a comment to a post            |
| GET    | `/api/comments/:postId`      | Get all comments for a post        |
| DELETE | `/api/comments/:commentId`   | Delete your own comment            |

---

### **6. Follow Routes**
Following system.

| Method | Route                        | Description                          |
|--------|------------------------------|--------------------------------------|
| POST   | `/api/follow/:userId`        | Follow a user                        |
| DELETE | `/api/follow/:userId`        | Unfollow a user                      |
| GET    | `/api/follow/followers/:userId` | Get followers of a user          |
| GET    | `/api/follow/following/:userId` | Get users a user is following     |

---

### **7. Notification Routes**
Real-time or in-app notifications.

| Method | Route                 | Description                          |
|--------|-----------------------|--------------------------------------|
| GET    | `/api/notifications`  | Get all notifications for current user |
| PATCH  | `/api/notifications/:id/read` | Mark notification as read       |

---

### **8. Upload Routes**
Media upload for posts and avatars.

| Method | Route                 | Description                          |
|--------|-----------------------|--------------------------------------|
| POST   | `/api/upload/post`    | Upload image/video for a post        |
| POST   | `/api/upload/avatar`  | Upload profile picture               |

---

### **9. Explore/Search Routes**
Explore trending posts or search content.

| Method | Route                     | Description                            |
|--------|---------------------------|----------------------------------------|
| GET    | `/api/explore/trending`   | Get trending/popular posts             |
| GET    | `/api/explore/posts?q=`   | Search posts by caption or hashtag     |

---

### **10. Messaging (Future - Optional)**
DM system if added later.

| Method | Route                          | Description                       |
|--------|--------------------------------|-----------------------------------|
| POST   | `/api/messages/:userId`        | Send message to a user            |
| GET    | `/api/messages/:userId`        | Get message thread with a user    |
| GET    | `/api/messages`                | Get all message threads           |
