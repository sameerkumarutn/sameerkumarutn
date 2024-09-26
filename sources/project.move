module MyModule::IdentityVerification {

    use aptos_framework::signer;
    use aptos_framework::coin;
    use std::option;

    /// Struct representing a user's identity verification status.
    struct VerifiedUser has store, key {
        is_verified: bool,     // Verification status
        verifier: address,     // The address of the entity that verified the user
    }

    /// Function to verify a user's identity.
    public fun verify_user(verifier: &signer, user: address) {
        let verification = VerifiedUser {
            is_verified: true,
            verifier: signer::address_of(verifier),
        };
        move_to(verifier, verification);
    }

    /// Function to check if a user is verified.
    public fun check_verification(user: address): bool acquires VerifiedUser {
        let verified_user = borrow_global<VerifiedUser>(user);
        verified_user.is_verified
    }
}
