// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract CorrectionRegistry {
    struct Correction {
        bytes32 oldHash;
        bytes32 newHash;
        address issuer;
        uint256 correctedAt;
    }

    mapping(bytes32 => Correction) public corrections;

    event CertificateCorrected(bytes32 indexed oldHash, bytes32 indexed newHash, address issuer, uint256 timestamp);

    function recordCorrection(bytes32 oldHash, bytes32 newHash) external {
        corrections[oldHash] = Correction({
            oldHash: oldHash,
            newHash: newHash,
            issuer: msg.sender,
            correctedAt: block.timestamp
        });

        emit CertificateCorrected(oldHash, newHash, msg.sender, block.timestamp);
    }

    function getCorrection(bytes32 oldHash) external view returns (bytes32, uint256) {
        Correction memory corr = corrections[oldHash];
        return (corr.newHash, corr.correctedAt);
    }
}
