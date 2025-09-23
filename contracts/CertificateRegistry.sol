// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract CertificateRegistry {
    struct Certificate {
        bytes32 certHash;
        address issuer;
        uint256 issuedAt;
        bool revoked;
    }

    mapping(bytes32 => Certificate) public certificates;

    event CertificateIssued(bytes32 indexed certHash, address issuer, uint256 timestamp);
    event CertificateRevoked(bytes32 indexed certHash, address issuer, uint256 timestamp);

    function issueCertificate(bytes32 certHash) external {
        require(certificates[certHash].issuedAt == 0, "Certificate already exists");

        certificates[certHash] = Certificate({
            certHash: certHash,
            issuer: msg.sender,
            issuedAt: block.timestamp,
            revoked: false
        });

        emit CertificateIssued(certHash, msg.sender, block.timestamp);
    }

    function revokeCertificate(bytes32 certHash) external {
        require(certificates[certHash].issuedAt != 0, "Certificate not found");
        require(!certificates[certHash].revoked, "Already revoked");

        certificates[certHash].revoked = true;
        emit CertificateRevoked(certHash, msg.sender, block.timestamp);
    }

    function verifyCertificate(bytes32 certHash) external view returns (bool, bool) {
        Certificate memory cert = certificates[certHash];
        if (cert.issuedAt == 0) {
            return (false, false); // not found
        }
        return (true, !cert.revoked);
    }
}
