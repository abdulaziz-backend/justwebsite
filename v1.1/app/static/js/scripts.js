function openModal() {
    document.getElementById('modal').style.display = 'block';
}

function closeModal() {
    document.getElementById('modal').style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function() {

    if (document.body.classList.contains('friends-page')) {
        handleFriendsPage();
    }
});

function handleFriendsPage() {
    const friendsList = document.querySelector('.friends-list');
    const noFriendsMessage = document.querySelector('.no-friends-message');

    if (friendsList && friendsList.children.length > 0) {
        friendsList.style.display = 'block';
        noFriendsMessage.style.display = 'none';
    } else if (noFriendsMessage) {
        noFriendsMessage.style.display = 'block';
    }

    const friendItems = document.querySelectorAll('.friend-item');
    friendItems.forEach(item => {
        item.addEventListener('click', function() {
            const username = this.getAttribute('data-username');
            alert(`You clicked on ${username}`);
        });
    });
}
    const loadingElement = document.getElementById('loading');
    if (loadingElement) {
        loadingElement.style.display = 'none';
    }



    document.addEventListener('DOMContentLoaded', function() {
        if (document.body.classList.contains('friends-page')) {
            handleFriendsPage();
        }
    });
    
    function handleFriendsPage() {
        const friendsListContainer = document.getElementById('friends-list-container');
        
        if (friendsListContainer) {
            const friends = friendsListContainer.querySelectorAll('li');
            
            if (friends.length > 0) {
                friendsListContainer.style.display = 'block';
            } else {
                friendsListContainer.innerHTML = '<h2>You have no friends yet!</h2><p>Invite friends to join and start earning together.</p>';
            }
        }
    
        const inviteButton = document.querySelector('.invite-button');
        if (inviteButton) {
            inviteButton.addEventListener('click', function() {
                // Handle invite button click
                alert('Invite your friends to join and earn $BLAZE!');
  
            });
        }
    }
